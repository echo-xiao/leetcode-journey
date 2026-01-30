class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        for i in range(len(recipes)):
            graph[recipes[i]] = ingredients[i]

        suppSet = set()
        for s in supplies:
            suppSet.add(s)

        status = {}
        res = []

        for i in range(len(recipes)):
            target = recipes[i]
            if self.dfs(target, graph, suppSet, status):
                res.append(target)

        return res

    def dfs(self, name, graph, suppSet, status):
        if name in suppSet:
            return True

        if name not in graph:
            return False

        if name in status:
            currState = status[name]
            if currState == 1:
                return False
            if currState == 2:
                return True
            if currState == 3:
                return False

        status[name] = 1

        needed = graph[name]

        for i in range(len(needed)):
            ing = needed[i]
            if self.dfs(ing, graph, suppSet, status) == False:
                status[name] = 3
                return False

        status[name] = 2
        return True
































