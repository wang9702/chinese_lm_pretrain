# 基于pytorch的中文语言模型预训练

### 介绍

ACL2020 Best Paper有一篇论文提名奖，《Don’t Stop Pretraining: Adapt Language Models to Domains and Tasks》。这篇论文做了很多语言模型预训练的实验，系统的分析了语言模型预训练对子任务的效果提升情况。有几个主要结论：
* 在目标领域的数据集上继续预训练（DAPT）可以提升效果；目标领域的语料与RoBERTa的原始预训练语料越不相关，DAPT效果则提升更明显。
* 在具体任务的数据集上继续预训练（TAPT）可以十分“廉价”地提升效果。

### 参考

- https://github.com/zhusleep/pytorch_chinese_lm_pretrain
- https://github.com/huggingface/transformers/blob/main/examples/pytorch/language-modeling
- https://blog.csdn.net/weixin_44217936/article/details/125707581

### 使用

```python
sh run.sh
```

### 与transformers v3.x不同的地方

- prediction_loss_only=True被移除了
- trainer.is_world_master()替换为trainer.is_world_process_zero()
- tokenizer.max_len替换为tokenizer.model_max_length
