def extend(class_to_extend):
    def decorator(extending_class):
        class_to_extend.__dict__.update(extending_class.__dict__)
        return class_to_extend
    return decorator

