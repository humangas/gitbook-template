# uml 
<!-- toc -->

## See also

- [PlantUML](http://plantuml.com/)
- [gitbook-plugin-uml](https://plugins.gitbook.com/plugin/uml)


## Status 

```uml
@startuml
testdot
@enduml
```

```
@startuml
testdot
@enduml
```

## Class diagram

```uml
@startuml

	Class Stage
	Class Timeout {
		+constructor:function(cfg)
		+timeout:function(ctx)
		+overdue:function(ctx)
		+stage: Stage
	}
 	Stage <|-- Timeout

@enduml
```

```
@startuml

	Class Stage
	Class Timeout {
		+constructor:function(cfg)
		+timeout:function(ctx)
		+overdue:function(ctx)
		+stage: Stage
	}
 	Stage <|-- Timeout

@enduml
```

