class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)

        for recipe, ingredientsList in zip(recipes, ingredients):
            indegree[recipe] = len(ingredientsList)
            for ing in ingredientsList:
                graph[ing].append(recipe)

        queue = collections.deque(supplies)
        ans = []
        recipeSet = set(recipes)

        while queue:
            curr = queue.popleft()
            if curr in recipeSet:
                ans.append(curr)

            for nextRecipe in graph[curr]:
                indegree[nextRecipe] -= 1
                if indegree[nextRecipe] == 0:
                    queue.append(nextRecipe)

        return ans