import talib

class TALibGuide: 
    @classmethod
    def getGroups(cls):
        for group in talib.get_function_groups().keys():
            print(group)

    @classmethod
    def getFunctions(cls, group):
        """
        Get the functions in a specific group.
        Args:
            group (str): The group name.
        """
        if group not in talib.get_function_groups():
            raise ValueError(f"Group '{group}' not found.")
        return talib.get_function_groups()[group]
    

