# Pycharm-Projects-100-Days-Code

## Best Practices

- When using methods you didn't write, use keyword parameters so it is clear what you are passing to the method
- If you only need 1 or 2 items from an imported module, use `import module_name`
  - But if you are going to be using many items from that module, be specific using the `from module_name import xyz, abc` so that you don't have to use `module_name.something` all the time
- Don't do `from module import *` because it might be confusing where you get items from
- All method names and variable names should use snake case (`hello_world`)
- All class names should use Pascal Case (`HelloWorld`)

## Class Inheritence 

```python

class Fish(Animal):

    def __init__(self):
        super().__init__()
```

The `Fish` Class inherits from the `Animal` class. To do this, pass in the `Animal` class to the `Fish` class and include `super().__init__()` in the constructor