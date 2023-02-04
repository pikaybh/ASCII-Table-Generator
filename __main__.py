from time import perf_counter

class ASCIICodeGenerator():
    '''
    Makes ASCII Code Table Object for a chart in a file with extension of `.md`.
    '''
    def __init__(self, initial_num=1, column=5, final_num=159):
        self.t_start = perf_counter()
        self.initial_num = initial_num
        self.column = column
        self.final_num = final_num
        self._range = (self.final_num - self.initial_num + 1)
        if self._range % self.column:
            self._true_div = self._range // self.column + 1
        else:
            self._true_div = self._range // self.column

    def mk_heading(self) -> str:
        '''
        Generates headings of the chart.
        '''
        return "| DEC | ASCII "*self.column + "|\n|" + ":--:|"*2*self.column + "\n"

    def ascii_table_gen(self) -> str:
        '''
        Generates the contents of ascii table
        '''
        s = ""
        for i in range(self.initial_num, self._true_div + 1):
            for j in range(i, i + (self._true_div * self.column), self._true_div):
                s += "| " + str(j) + " | `" +  chr(j) + "` "
            s += " |\n"

        if self.final_num % self._true_div:
            s += "| " * (self.column - (self.final_num % self._true_div)) + "|"

        return s

    def __str__(self):
        return self.mk_heading() + self.ascii_table_gen()

    def __del__(self):
        print(f"process done in {(perf_counter() - self.t_start):.5f} milliseconds.")


if __name__ == "__main__":
    print(ASCIICodeGenerator())