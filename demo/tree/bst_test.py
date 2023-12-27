from bst import BST

def main():
    test_bst = BST([3, 8, 2, 6, 1, 9, 4, 9, 5])
    # The BST should look like:
    #       3
    #     2   8
    #    1   6 9
    #       4
    #        5
    print(test_bst.sorted())
    # 为了检查BST是否如我们的期望, 可以level_order一下, 结果应该是：328169945
    print(test_bst.check_BST())
    search_test = [3, 9, 10]
    for val in search_test:
        print(f'{val} appeared {test_bst.search(val)} times.')
    
    print("Testing left rotate:")
    test_bst.lr_whole()
    print(test_bst.sorted()) # 排序仍然是正确的
    print(test_bst.check_BST()) # 应该是 839926145

    print("Testing right rotate:")
    test_bst.rr_whole()
    print(test_bst.sorted()) # 排序仍然是正确的
    print(test_bst.check_BST()) # 应该变回了 328169945

    test_bst.delete(9) # 删除一个多次出现的值
    print(test_bst.check_BST()) # 现在应该是32816945
    test_bst.delete(1) # 删除一个叶节点
    print(test_bst.check_BST()) # 现在应该是3286945
    test_bst.delete(3) # 删除整个的根节点
    print(test_bst.check_BST()) # 现在应该是869425
    print(test_bst.sorted()) # 顺序仍然是对的

if __name__ == "__main__":
    main()