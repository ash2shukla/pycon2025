---
marp: true
paginate: true
footer: Creative Commons Attribute - ShareAlike 4.0 International (CC BY-SA 4.0)
---

# Understanding Plugin Architecture for Python Packages

**Ashish Shukla**
Lead Software Engineer
EPAM Systems

![bg right:50%](bg.png)

<br/>

![w:128](epam_logo.png)

---

# Overview
#### How plugins work in Python
- What and Why Plugins ? 
- Some Examples
- Plugin Loader from SQLAlchemy
- Python package entrypoints and importlib.metadata

#### How you can make it work for your package
- Creating a hello world package
- Creating plugin structure and plugin loader utils
- Extending hello world package with hello-world-kannada-plugin

---

# What and Why Plugins ?
- What ?
> Plugins are a way to extend something.
- Why ?
    1. Keeping core package slim
    2. Let the users decide what they want
    3. Extensibility
    4. Decouple core logic and implementations
    5. Get contributions !

---

# Some Examples

## SQLAlchemy Dialects

You can install additional dialects in SQLAlchemy like Clickhouse, GSheet, Druid etc. and extend the set of default supported dialects.

## Airflow Providers

You can extend airflow's supported operators, hooks, connections etc. by installing new providers. eg. Google, AWS etc.

---

# Plugin Loader from SQLAlchemy

```python
from importlib import metadata as importlib_metadata

class PluginLoader:
    def __init__(self, group):
        self.group = group
        self.impls = {}

    def load(self, name):
        if name in self.impls:
            return self.impls[name]()
        
        entrypoints = importlib_metadata.entry_points()                                        
        impls = entrypoints.select(group=self.group)
        for impl in impls:
            if impl.name == name:
                self.impls[impl.name] = impl.load
                return impl.load()
        
        raise ValueError("No such plugin!")
```

---

# Python Package Entrypoints and Importlib Metadata

## Entrypoints
(From Python packaging user guide](https://packaging.python.org/en/latest/specifications/entry-points/)
> Entry points are a mechanism for an installed distribution to advertise components it provides to be discovered and used by other code.


---
# Python Package Entrypoints and Importlib Metadata

## How to declare it in pyproject.toml
```python
[project.entry-points.group_name]
name = path_to_object
```

## How to declare it in setup.py
```python
entry_points={
    'group_name': [
        'key = path.to:Callable',
    ],
},
```

---

# How you can make it work for your package

#### Using the same logic for our own plugins
1. Let others know how they can create code for you
    - Plugin Interface
2. Give them an identifier so that they can tell their code is for your package
    - Entrypoint Group Name
3. Write some code that can load `their code`
    - Plugin Loader
4. Use others' code !


---
# How you can make it work for your package

#### Coding time !!

---
# Conclusion
1. Plugins = Extensibility
2. Entrypoints = Python native way of implementing plugins
3. Result = Long Live your future package !

---
# References
1. SQLAlchemy - https://github.com/zzzeek/sqlalchemy
    1. [Dialects](https://github.com/sqlalchemy/sqlalchemy/blob/main/lib/sqlalchemy/engine/interfaces.py#L641)
    2. [External Dialects List](https://docs.sqlalchemy.org/en/20/dialects/index.html#external-dialects)
    3. [Create Engine Implementation](https://github.com/zzzeek/sqlalchemy/blob/main/lib/sqlalchemy/engine/create.py#L116)

2. Airflow - https://github.com/apache/airflow
3. Python Packaging Guide - https://packaging.python.org/en/latest/

---

![bg right:50%](bg.png)

# Thanks !
# Questions ?

Code and slides at: https://github.com/ash2shukla/pycon2025
Connect with me: https://linkedin.com/in/ash2shukla
