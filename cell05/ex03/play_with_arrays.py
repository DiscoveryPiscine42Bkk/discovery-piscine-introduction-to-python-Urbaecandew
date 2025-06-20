def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    print(original_array)
    transformed = [x + 2 for x in original_array if x > 5]
    result_set = set(transformed)
    print(result_set)

if __name__ == "__main__":
    main()
