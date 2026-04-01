import numpy as np
import matplotlib.pyplot as plt
import function as f
import random 

def a1_and_a2(K = 5,distribution = f.make_distribution(5),save_fig = True):
    #定数
    count = K

    #使うリスト
    #LCB UCB周り
    LCB = [0 for i in range(K)] ; UCB = [100 for i in range(K)] ; idx = LCB.index(max(LCB)) ; UCB_others = UCB[:idx] + [] + UCB[idx:]

    #カウント用
    each_attempt = [1 for i in range(K)]
    each_result = [np.random.binomial(1,distribution[i]) for i in range(K)]
    each_average = [each_result[i]/each_attempt[i] for i in range(K)]

    while max(LCB)<max(UCB_others):
        a1 = random.choice(f.max_idx(each_average))
        a2 = random.choice(f.max_idx(UCB,a1))

        for i in [a1,a2]:
            each_attempt[i] += 1
            each_result[i] += np.random.binomial(1,distribution[i])

            UCB[i] = f.UCBi(each_attempt,each_result,i)
            LCB[i] = f.LCBi(each_attempt,each_result,i)

        idx = LCB.index(max(LCB)) ; UCB_others = UCB.copy()
        UCB_others[idx] = 0
        each_average = [each_result[i]/each_attempt[i] for i in range(K)]
        count += 2
    for i in range(K):
        UCB[i] = f.UCBi(each_attempt,each_result,i)
        LCB[i] = f.LCBi(each_attempt,each_result,i)

    if save_fig:
        fig,ax = plt.subplots()
        for i in range(K):
            ax.plot([UCB[i],LCB[i]],[i,i],marker = "|")
            ax.plot(each_average[i],i,marker = "o",color = "black")
        ax.set_box_aspect(1)
        plt.savefig(f"graphs/graph(a1_and_a2).png",dpi = 600, bbox_inches="tight")

    return count,distribution.index(max(distribution)) == each_average.index(max(each_average))

if __name__ == "__main__":
    a1_and_a2()
