#From https://github.com/ufal/multilexnorm2021/blob/master/callbacks/checkpoint_callback.py
import pytorch_lightning as pl

class CheckpointCallback(pl.Callback):
    def __init__(self, args):
        super().__init__()
        self.language = args.dataset.language
        self.model_name = args.model.pretrained_lm.split('/')[-1]

    def on_train_epoch_end(self, trainer, pl_module, unused=None):
        if not trainer.is_global_zero or pl_module.is_finetuning:
            return

        directory = f"checkpoints_last/{self.language}/{self.model_name}_wiki_5_epoch-{pl_module.current_epoch}"
        pl_module.model.save_pretrained(directory)
