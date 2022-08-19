class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.apps = []
        self.is_on = False

    def install(self, app, app_memory):
        if self.memory >= app_memory:
            if self.is_on:
                self.apps.append(app)
                self.memory -= app_memory
                return f"Installing {app}"
            else:
                return f"Turn on your phone to install {app}"
        return f"Not enough memory to install {app}"

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def status(self):
        total_apps_count = len(self.apps)
        memory_left = self.memory
        return f"Total apps: {total_apps_count}. Memory left: {memory_left}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())