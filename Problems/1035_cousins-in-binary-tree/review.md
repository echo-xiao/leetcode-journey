# 1035. 二叉树的堂兄弟节点 · 复盘

这个里面既可以用dfs，也可以用bfs，semantics是通过traverse一遍树，获取x和y的信息，层级以及值，然后判断这两个是否在同一层，并且是否不是同一个父节点。所以这个里面主体是traverse是个辅助函数，遍历整个tree，如果是x的话，记录他的父节点和level层级信息，如果是y的话，同样的操作，然后再递归子树，子树里面的prev和level参数，由于一个是str，一个是int，所以需要传递新的值，比如当从node移动到node.left的时候，调用的就是traverse(node.left, node, level+1)，这里的node成了父节点，level+1成了新的层级。traverse函数仅仅需要遍历，node节点不需要额外的子孙树返回值做决策，不需要子孙树的信息，所以traverse这个函数是没有返回值的。termiantion case就是base case。但是isCousins是用来做最后做决策的，所以全局变量的信息，来判断x和y是否在同一层但是不同的父节点，isCousins返回的就只是基本的层级是否相等，但是不同父节点的信息。
