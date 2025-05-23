class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.inferred = set()

    def add_fact(self, predicate, *args):
        self.facts.add((predicate, *args))

    def query(self, predicate, *args):
        return (predicate, *args) in self.facts or (predicate, *args) in self.inferred

    def infer(self):
        new_inferred = set()

        for fact in list(self.facts) + list(self.inferred):
            pred, a, b = fact

            if pred == "likes" and a == "mary":
                new_inferred.add(("likes", "john", b))

            if pred == "likes" and b == "wine":
                new_inferred.add(("likes", "john", a))

            if pred == "likes" and a == b:
                new_inferred.add(("likes", "john", a))

        changed = True
        while changed:
            changed = False
            temp = set()
            for fact in new_inferred:
                if fact not in self.inferred:
                    self.inferred.add(fact)
                    changed = True
                    temp.add(fact)
            new_inferred = set()
            for fact in temp:
                pred, a, b = fact
                if pred == "likes" and a == "mary":
                    new_inferred.add(("likes", "john", b))
                if pred == "likes" and b == "wine":
                    new_inferred.add(("likes", "john", a))
                if pred == "likes" and a == b:
                    new_inferred.add(("likes", "john", a))

    def show_likes(self, person):
        result = [b for (pred, a, b) in self.facts.union(self.inferred) if pred == "likes" and a == person]
        return set(result)


kb = KnowledgeBase()
kb.add_fact("likes", "mary", "food")
kb.add_fact("likes", "mary", "wine")
kb.add_fact("likes", "john", "wine")
kb.add_fact("likes", "john", "mary")

kb.infer()

print("John likes:", kb.show_likes("john"))
