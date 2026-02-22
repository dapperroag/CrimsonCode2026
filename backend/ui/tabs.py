class TabManager:
    def __init__(self):
        self.tab_inputs = [""]
        self.current_index = 0
    
    #Returns the new index of the new tab
    def add_tab(self):
        self.tab_inputs.append("") #add the new string
        self.current_index = len(self.tab_inputs) - 1 #adjust the index
        return self.current_index

    def delete_tab(self, target_index):
        if len(self.tab_inputs) > 1:
            self.tab_inputs.pop(target_index)
            self.current_index = max(0, self.current_index - 1)

    #Returns the string of the targeted tab
    def switch_tab(self, target_index, current_string):
        self.tab_inputs[self.current_index] = current_string
        self.current_index = target_index
        return self.tab_inputs[target_index]
        