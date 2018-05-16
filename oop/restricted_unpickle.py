
import builtins
import pickle
class RUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        if module == "builtins":
            if name not in ("exec", "eval"):
                return getattr(builtins, name)
        elif module == "__main__":

            return globals()[name]
        
        raise pickle.UnpicklingError("global '{module}.{name}, is forbidden"\
                                     .format(module=module, name= name))
    

    
"""
using is like folowing

with open ("file.p", "rb") as f:
    objects = RUnpickler(f).load()
"""
