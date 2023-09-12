from utils import read_data, get_executed_operations, get_sorted_operations, get_operation_info


def main():
    all_operations = read_data('operations.json')
    executed_operations = get_executed_operations(all_operations)
    sorted_operations = get_sorted_operations(executed_operations)
    five_operations = sorted_operations[0:5]
    for operation in five_operations:
        print(get_operation_info(operation))


if __name__ == '__main__':
    main()




