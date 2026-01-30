class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for ingredientList, recipt in zip(ingredients, recipes):
            indegree[recipt] = len(ingredientList)
            for ing in ingredientList:
                graph[ing].append(recipt)

        queue = collections.deque(supplies)
        recipeSet = set(recipes)
        ans = []

        while queue:
            curr = queue.popleft()
            
            if curr in recipeSet:
                ans.append(curr)

            for nextRecipt in graph[curr]:
                indegree[nextRecipt] -= 1
                if indegree[nextRecipt] == 0:
                    queue.append(nextRecipt)
        return ans
                