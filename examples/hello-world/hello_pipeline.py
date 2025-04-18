from kfp import dsl

@dsl.component(
        base_image='docker-registry.qualcomm.com/library/python:3.10-slim'
)
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@dsl.pipeline
def hello_pipeline(recipient: str) ->str:
    hello_task = say_hello(name=recipient)
    return hello_task.output

from kfp import compiler
if __name__ == '__main__':
    compiler.Compiler().compile(
        pipeline_func=hello_pipeline,
        package_path='hello_pipeline.yaml'
    )
    print("Pipeline compiled successfully!")