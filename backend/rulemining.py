import sys

def load_dataset(fname):
    dataset = []
    f = open(fname,"r")
    for line in f:
        dataset.append(line.rstrip("\n").split(",")[:-1])
    #print dataset
    return dataset

outfile = None
freq = []

ruleTable = dict()

def getAprioriTxns(freq_sets, k):
    retList = []
    lenLk = len(freq_sets)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            L1 = list(freq_sets[i])[:k - 2]
            L2 = list(freq_sets[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(freq_sets[i] | freq_sets[j])
    return retList


def apriori(dataset, minsupport=0.3):
    print "Generate a list of candidate item sets"
    C1 = createC1(dataset)
    D = map(frozenset, dataset)
    L1, support_data = scanD(D, C1, minsupport)
    L = [L1]
    k = 2
    while (len(L[k - 2]) > 0):
        Ck = getAprioriTxns(L[k - 2], k)
        Lk, supK = scanD(D, Ck, minsupport)
        support_data.update(supK)
        L.append(Lk)
        k += 1

    return L, support_data


def generateRules(L, support_data, minConfidence=0.3):

    rules = []
    for i in range(1, len(L)):
        for freqSet in L[i]:
            H1 = [set([item]) for item in freqSet]
            freq.append(("freqSet", freqSet, 'H1', H1))
            if (i > 1):
                getCandidateRules(freqSet, H1, support_data, rules, minConfidence)
            else:
                getConfidence(freqSet, H1, support_data, rules, minConfidence)
    return rules


def getConfidence(freqSet, H, support_data, rules, min_confidence=0.1):
    print "Evaluate the rule generated"
    pruned_H = []
    for conseq in H:
        conf = support_data[freqSet] / support_data[freqSet - conseq]
        if conf >= min_confidence:
            #print freqSet - conseq, '--->', conseq, 'conf:', conf
            key = sorted(freqSet-conseq)
            if(not ruleTable.get(",".join(key),False)):
				ruleTable[",".join(key)]=list();
            ruleTable[",".join(key)].append([",".join(conseq),str(conf)])
            outfile.write(str(freqSet - conseq) +  '--->'+ str(conseq)+ 'conf:' + str(conf))
            outfile.write("\n")
            rules.append((freqSet - conseq, conseq, conf))
            pruned_H.append(conseq)
    return pruned_H


def getCandidateRules(freqSet, H, support_data, rules, min_confidence=0.3):
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = getAprioriTxns(H, m + 1)
        Hmp1 = getConfidence(freqSet, Hmp1, support_data, rules, min_confidence)
        if len(Hmp1) > 1:
            getCandidateRules(freqSet, Hmp1, support_data, rules, min_confidence)


def createC1(dataset):
    c1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in c1:
                c1.append([item])
    c1.sort()
    return map(frozenset, c1)


def scanD(dataset, candidates, min_support):
    sscnt = {}
    for tid in dataset:
        for can in candidates:
            if can.issubset(tid):
                sscnt.setdefault(can, 0)
                sscnt[can] += 1

    num_items = float(len(dataset))
    retlist = []
    support_data = {}
    for key in sscnt:
        support = sscnt[key] / num_items
        if support >= min_support:
            retlist.insert(0, key)
        support_data[key] = support
    return retlist, support_data



if __name__ ==  "__main__":
    args = sys.argv
    outfile = open(args[3],'w')
    dataset = load_dataset(args[1])
    L,support_data = apriori(dataset,float(args[2]))
    generateRules(L,support_data,float(args[2]) )
    outfile.write("\n")
    printarray = []
    print ruleTable;
    for i in support_data.keys():
       # print support_data[i]
        if support_data[i] > float(args[2]):
            printarray.append( str(i) +" : " + str(support_data[i]))


    for i in printarray:
        outfile.write(i+"\n")
    outfile.close()
