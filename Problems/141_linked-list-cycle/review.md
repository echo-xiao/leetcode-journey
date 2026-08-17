# 141. 环形链表 · 复盘

这个一看判断是否有环，就是快慢指针了，这个里面就是写loop的时候条件需要注意是 while fast is not none and fast.next is not none 这种情况，因为slow走一步，fast走两步，首先fast肯定走的比slow快，所以只要考虑fast的情况，因为fast不为none的话，slow肯定不是none，然后fast走两步就意味着fast.next不能够是none，如果fast.next是none的话，none的next就会报错。fast.next不是none，就意味着fast不能是none，不然fast.next就会报错。所以是不是只要有fast.next.next这种写法的，while loop都是fast is not none and fast.next is not none？gemini说是的。
