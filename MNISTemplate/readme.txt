source: https://github.com/ashleve/lightning-hydra-template
sub-source: https://github.com/domenicocinque/minimal-lightning-hydra-template

to study:
- https://docs.wandb.ai/ref/python/public-api/sweep
- https://docs.wandb.ai/guides/sweeps/define-sweep-configuration#command
- https://github.com/captain-pool/hydra-wandb-sweeper


Use the wandb sweep command to initialize a sweep. The proceeding code example initializes a sweep for a sweeps_demo project and uses a config.yaml file for the configuration.

```shell
wandb sweep --project sweeps_demo configs/sweep.yaml
```
This command will print out a sweep ID. The sweep ID includes the entity name and the project name. Make a note of the sweep ID.

Start sweep agents:
```shell
wandb agent entity/project/sweep_ID
```
where entity is your W&B username, project is the name of the project you created, and sweep_ID is the ID of the sweep you created.