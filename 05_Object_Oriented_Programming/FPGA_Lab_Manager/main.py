    # FPGA Lab Manager
    # Main

    from fpga import FPGA
    from lab import FPGALab

    lab = FPGALab("AI Hardware Lab")

    def get_integer(message):

        while True:

            try:
                value = int(input(message))
                return value

            except ValueError:
                print("Please Enter a Valid Number!")

    while True:

        print("================")
        print("FPGA Lab Manager")
        print("================")
        print()
        print("1. Add FPGA")
        print("2. Show FPGA")
        print("3. Find FPGA")
        print("4. Remove FPGA")
        print("5. Power Report")
        print("6. Exit")


        option = get_integer("Select an Option: ")

        if option < 1 or option > 6:

            print("Invalid Input")
            continue

        if option == 1:

            fpga_name = input("Enter FPGA Name: ")
            fpga_vendor = input("Enter FPGA Vendor: ")
            fpga_frequency = get_integer("Enter FPGA Frequency: ")
            fpga_power = get_integer("Enter FPGA Power: ")
            fpga_luts = get_integer("Enter FPGA LUTs Number: ")
            fpga = FPGA(fpga_name, fpga_vendor, fpga_frequency, fpga_power, fpga_luts)
            lab.add_fpga(fpga)

        elif option == 2:

            lab.show_all()

        elif option == 3:

            name = input("Enter FPGA Name: ")
            result=lab.find_fpga(name)
            if result:
                print("This is what you are looking for: ")
                print(result)
            else:
                print("FPGA Not Found!")

        elif option == 4:

            name = input("Enter FPGA name to Remove: ")
            fpga = lab.find_fpga(name)

            if fpga:
                lab.remove_fpga(fpga)
            else:
                print("FPGA Not Found!")

        elif option == 5:

            lab.power_report()

        elif option == 6:

            print("Exiting FPGA Lab...")
            break

