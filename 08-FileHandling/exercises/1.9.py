def main():
    file_name = 'it_company.csv' # z jakiegos powodu w szablonie zadania bylo .txt
    job_title = 'Software Engineer'
    counter = 1

    with open(file_name, 'r') as file:
        for line in file:
            if job_title in line:
                print(f"{counter}. {line}", end="")
                counter += 1

if __name__ == "__main__":
    main()