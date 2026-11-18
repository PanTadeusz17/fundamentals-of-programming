def main():
    employees_file = 'it_company.csv'
    position_file = 'software_engineer.txt'
    job_title = 'Software Engineer'

    with open(employees_file, 'r') as source:
        with open(position_file, 'w') as target:
            for line in source:
                if job_title in line:
                    target.write(line)

if __name__ == "__main__":
    main()