#                               Finding and fixing bugs in your code(Debugging)
# * Describe the problem and test your assumption to see which is false.
# * Reproduce the bug: Some bugs are sneaky they only occur under certain conditions. In order to debug them, we need to be able to
#reliably reproduce the bug and diagnose our problem to figure out which condition triggered the bug.
# * Playing Computer: This is an important skill in debugging, you need to be able to go through your code line by line as if you were
#the computer to help you figure out what is going wrong.
# * Fix any red underlines that show up in the editor before you run your code. The yellow underlines are optional fixes, sometimes
#it will cause a problem down the line, and other times it won't. It could just mean that the editor doesn't understand what you are
#trying to do.
# * Use the print statement to see your code that is not throwing any error but is not doing what you want it to do.
# * Most IDEs (Intelligent Development Environment): Most IDEs such as pycharm, VS Code will have builtin tools for debugging. This is
#normally known as the debugger in many ways they are the print statement

#                                  Debuggers
# - Debuggers: They allow us to peek into our code during execution and pause on chosen lines to figure out what is the inner
#mechanism and where it is going wrong. They are couple things that are the same in most IDEs which you should be familiar with:
# * Breakpoint: You can set a breakpoint by clicking on a line in the gutter of your code.
# * Step Over: This button will go through the execution of your code line by line stopping at the very next line and allows
#you to view the intermediate values of your variables.
# * Step into: This will enter into any other modules that your code references. For example, if you use a function from the random
#module, it will show you the original code for that function so you can better understand its functionality.
# * Step into my code: This does the same thing as a step into, but it limits the scope to your own project code and ignores library
#code such as random.