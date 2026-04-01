from a1_and_a2 import a1_and_a2
from a1_or_a2 import a1_or_a2
import function as f

def compare():
    K = 5
    distribution = f.make_distribution(5)
    count_and , frag_and = a1_and_a2(K,distribution)
    count_or , frag_or=a1_or_a2(K,distribution)
    print(f"frag_and:{frag_and},frag_or:{frag_or}")
    print(f"count_and:{count_and},count_or:{count_or}")
    faster = "and" if count_and < count_or else "or"
    print(f"faster one:{faster}")
    print(f"distribution{distribution}")

if __name__ == "__main__":
    compare()