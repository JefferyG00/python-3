# Function to flatten and sort a list of lists
def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

# Define the Podracer class
class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    # Define a repair method that will update the condition of the podracer to "repaired"
    def repair(self):
        self.condition = "repaired"
    
    # String representation for easy debugging and printing
    def __str__(self):
        return f"Podracer(max_speed={self.max_speed}, condition={self.condition}, price={self.price})"

# Define a new class AnakinsPod that inherits the Podracer class
class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    # Define a boost method that will multiply max_speed by 2
    def boost(self):
        self.max_speed *= 2

# Define another class SebulbasPod that inherits Podracer
class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    # Define a flame_jet method that will update the condition of another podracer to "trashed"
    def flame_jet(self, other):
        other.condition = "trashed"

# Create instances and demonstrate the functionality
if __name__ == "__main__":
    anakin_pod = AnakinsPod(max_speed=500, condition="perfect", price=1000)
    sebulba_pod = SebulbasPod(max_speed=450, condition="perfect", price=1200)
    
    print("Before boost and flame_jet:")
    print(anakin_pod)
    print(sebulba_pod)
    
    anakin_pod.boost()
    sebulba_pod.flame_jet(anakin_pod)
    
    print("\nAfter boost and flame_jet:")
    print(anakin_pod)
    print(sebulba_pod)
    
    anakin_pod.repair()
    
    print("\nAfter repair:")
    print(anakin_pod)
    print(sebulba_pod)
