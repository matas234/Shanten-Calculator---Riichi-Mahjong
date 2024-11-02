def calculateShanten(hand_array, numCalledMelds=0):    
    def getPairs(suit_arr):
        possible_pairs=[]
        for i in range(9):
            if suit_arr[i]>1:
                out = [0]*9
                out[i] = 2
                possible_pairs.append(out)
        return possible_pairs
    
    def getTriplets(suit_arr):
        possible_triplets=[]

        for i in range(9):
            if suit_arr[i]>2:
                out = [0]*9
                out[i] = 3
                possible_triplets.append(out)
        return possible_triplets
    
    def completeSequences(suit_arr):
        possible_sequences=[]
        for i in range(2,9):
            if suit_arr[i]>0 and suit_arr[i-1]>0 and suit_arr[i-2]>0:
                out = [0]*9
                out[i]=1
                out[i-1]=1
                out[i-2]=1
                possible_sequences.append(out)
        return possible_sequences
    
    def incompleteSequences(suit_arr):
        possible_insequences=[]
        if suit_arr[0]>0 and suit_arr[1]>0:
            out = [0]*9
            out[0]=1
            out[1]=1
            possible_insequences.append(out)
        for i in range(2,9):
            if suit_arr[i]>0 and suit_arr[i-1]>0:
                out = [0]*9
                out[i]=1
                out[i-1]=1
                possible_insequences.append(out)
            if suit_arr[i]>0 and suit_arr[i-2]>0:
                out = [0]*9
                out[i]=1
                out[i-2]=1
                possible_insequences.append(out)
        return possible_insequences
    

    def splitsNoGroups(hand):
        maxTaatsuNum = 0
        maxPairPresence = False

        setInseqs = incompleteSequences(hand)
        setPairs = getPairs(hand)

        for pair in setPairs:
            currTaatsuNu = splitsNoGroups([h - p for h, p in zip(hand, pair)])[0] + 1
            if currTaatsuNu > maxTaatsuNum:
                maxTaatsuNum = currTaatsuNu
                maxPairPresence = True

        for inSeq in setInseqs:
            currTaatsuNum, currPairPresence = splitsNoGroups([h - i for h, i in zip(hand, inSeq)])
            currTaatsuNum += 1
            if currTaatsuNum > maxTaatsuNum:
                maxTaatsuNum = currTaatsuNum
                maxPairPresence = currPairPresence

        return maxTaatsuNum, maxPairPresence


    def splits(hand, groupNum=0, pair_presence=False):  
        maxGroupNum = groupNum
        maxTaatsuNum = 0
        maxPairPresence = pair_presence
        
        setSeqs = completeSequences(hand)
        setTriplets = getTriplets(hand)

        for meld in setSeqs + setTriplets:
            currGroupNum, currTaatsuNum, currPairPresence  = splits([h - m for h, m in zip(hand, meld)], 
                                                                    groupNum+1, 
                                                                    pair_presence)   
            
            if currGroupNum > maxGroupNum:
                maxGroupNum = currGroupNum
                maxTaatsuNum = currTaatsuNum
                maxPairPresence = currPairPresence

            elif currGroupNum == maxGroupNum:
                if currTaatsuNum > maxTaatsuNum:
                    maxTaatsuNum = currTaatsuNum
                    maxPairPresence = currPairPresence

                elif (currTaatsuNum == maxTaatsuNum) and (pair_presence):
                    maxTaatsuNum = currTaatsuNum
                    maxPairPresence = currPairPresence

 
        if (not setSeqs) and (not setTriplets):     #if no more groups then counts maximum of taatsu    
            maxTaatsuNum, maxPairPresence = splitsNoGroups(hand)

        return maxGroupNum, maxTaatsuNum, maxPairPresence


    def splitsTotal(hand):
        ## num of groups, num of taatsu, has pair
        totalSplit = [0,0,False]

        for suitTiles in hand[:3]:
            suitSplit = splits( hand=suitTiles )
            totalSplit[0] += suitSplit[0]
            totalSplit[1] += suitSplit[1]
            if suitSplit[2] == True:
                totalSplit[2] = True

        for honourTile in hand[3]:
            if honourTile == 3:
                totalSplit[0] += 1
            elif honourTile == 2:
                totalSplit[1] +=1
                totalSplit[2] = True

        return totalSplit


    def general_shanten(hand_array):
        totalSplit = splitsTotal(hand_array)
        tatNum = totalSplit[1]
        groupNum = totalSplit[0] + numCalledMelds
        pairPresence = totalSplit[2]
        p=0

        #checking for the edge cases:
        if (tatNum >= 5-groupNum) and (not pairPresence):
            p=1

        # using formula
        return 8 - 2*groupNum - min(tatNum, 4 - groupNum) - min(1, max(0, tatNum + groupNum - 4) ) + p


    def chiitoistu_shanten(hand_array):
        numPairs = 0
        for suit in hand_array:
            for tile in suit:
                numPairs += tile//2      #counts number of pairs, 4 of the same tile are treated as 2 pairs
    
        return 6 - numPairs


    def orphanSource_shanten(hand_array):
        diffTerminals = 0
        pairsTerminals = 0
        pairConstant = 0

        for i in [0,8]:                  #iterates over numbered suits
            for suit in hand_array[:3]:
                pairsTerminals += min(1, suit[i]//2)
                diffTerminals += min(1, suit[i])

        for num in hand_array[3]:        #iterates over honours
            pairsTerminals += min(1, num//2)
            diffTerminals += min(1, num//1)

        if pairsTerminals > 0:
            pairConstant=1

        return 13 - diffTerminals - pairConstant


    return min(general_shanten(hand_array), chiitoistu_shanten(hand_array), orphanSource_shanten(hand_array))

