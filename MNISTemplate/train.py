import logging
import warnings

import hydra

log = logging.getLogger(__name__)


@hydra.main(version_base="1.3", config_path="configs", config_name="train.yaml")
def main(cfg):
    warnings.filterwarnings("ignore", ".*does not have many workers.*")

    logger = hydra.utils.instantiate(cfg.logger)
    datamodule = hydra.utils.instantiate(cfg.data)
    model = hydra.utils.instantiate(cfg.model)
    trainer = hydra.utils.instantiate(cfg.trainer, logger=logger)

    trainer.fit(model=model, datamodule=datamodule)


if __name__ == "__main__":
    main()