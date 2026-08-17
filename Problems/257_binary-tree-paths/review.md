# 257. 二叉树的所有路径 · 复盘

semantics是 返回所有的从根到叶子节点的path，就是需要遍历从更节点到叶子节点的路径，并且将完整的路径字符串收集到外部列表res中。主体是有调用一个traverse的辅助函数，函数里面需要参数path能够传递父节点的信息，然后一个是全局的返回值res。python的参数调用里面，str是不可变的，但是list是可变的，所以这个里面path是str，所以需要构建新的new path，才能够赋值到子递归的参数里面去，但是res就不用了，可以直接复制到后面的子递归里面。主体就会是构建new path。termination case就是 1. base case，如果node为空，就返回，2. 如果到了叶子节点，那么就把构建好的new path增加到res这个list里面去。**#tree #backtracking**
