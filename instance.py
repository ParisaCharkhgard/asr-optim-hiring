class Machine:
    def __init__(self, available_day, purchase_price, resell_price, daily_profit):
        self.available_day = available_day
        self.purchase_price = purchase_price
        self.resell_price = resell_price
        self.daily_profit = daily_profit

    @classmethod
    def from_line(cls, line):
        available_day, purchase_price, resell_price, daily_profit = (
            int(i) for i in line.split()
        )
        return cls(available_day, purchase_price, resell_price, daily_profit)

    def __repr__(self):
        return f"Machine: {self.available_day}-{self.purchase_price}-{self.resell_price}-{self.daily_profit}"


class Instance:
    def __init__(
        self,
        case_number,
        number_of_machines,
        initial_budget,
        number_of_days,
        machine_list,
    ):
        self.case_number = case_number
        self.number_of_machines = number_of_machines
        self.initial_budget = initial_budget
        self.number_of_days = number_of_days
        self.machine_list = machine_list

    @property
    def instance_key(self):
        return f"Case {self.case_number}"

    @property
    def instance_summary(self):
        return f"{self.number_of_machines} {self.initial_budget} {self.number_of_days}"

    def __repr__(self):
        return f"Instance: {self.instance_key}"


def get_instance_list(filepath):
    """
    returns a list of instances from the input file
    """
    lines = None
    with open(filepath, "r") as f:
        lines = f.readlines()
    instance_list = []
    if not lines:
        return instance_list
    line_id = 0
    case_number = 0
    while True:
        line = lines[line_id]
        number_of_machines, initial_budget, number_of_days = (
            int(i) for i in line.split()
        )
        if number_of_machines < 0 or initial_budget < 0 or number_of_days < 0:
            raise "Invalid data."
        elif number_of_machines + initial_budget + number_of_days == 0:
            break
        last_machine_index = line_id + number_of_machines
        machine_list = []
        for i in range(line_id + 1, last_machine_index + 1):
            machine_list.append(Machine.from_line(lines[i]))
        case_number += 1
        instance_list.append(
            Instance(
                case_number,
                number_of_machines,
                initial_budget,
                number_of_days,
                machine_list,
            )
        )
        line_id = last_machine_index + 1

    return instance_list
