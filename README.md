# Pitchee 嗓音训练知识库

本知识库包含 49 篇中文文章，供 Pitchee 用户理解声音分析、探索个人声音目标、比较练习和了解何时寻求专业支持。文章于 2026-10-05 完成科学性与编辑修订；来源包括研究论文、专业实践资料、大学教学资源和社区经验，各自能支持的结论不同。

## 先分清这些概念

| 概念 | 在本文库中的含义 | 使用边界 |
|---|---|---|
| 音高 / F0 | 周期性发声的基频估计，单位 Hz | 不等于共鸣、音色或性别身份；算法可能漏检、倍频或半频误判 |
| 音色分（VFP） | 现有模型对音色女性向参考特征的评分 | 不是 F1–F4 共鸣分；可能系统性误判，重复结果也不保证正确 |
| 自然分（Naturalness） | 产品希望估计日常说话的自然听感及刻意、风格化程度 | 不是机器音检测；不能判断本人意图、肌肉状态或嗓音健康，也可能误判 |
| 目标方向综合分 | 按当前产品规则合成音色分、自然分、F0 等输入；不同方向公式不同 | 不完整测量语调、情感和语境，不是被他人识别为某个性别的概率 |
| 持续元音的共振峰分析 / 拟议共鸣分 | 针对指定元音估计 F1–F4，研究声道共振特征；评分需另行定义和验证 | 当前工作区没有独立元音选择与共鸣分功能，不能拿 VFP 代替；不能保证任何语境下的听感 |

高 F0、高音色分与低自然分可以同时出现。这个组合只是模型的多维反馈，不足以诊断发声方式。普通对话的目标听感还涉及韵律、重音、情感表达、语言和听者情境，不能压缩成单个声学指标。

**如果 VFP 与听感持续不符，可以跳过由它触发的文章。** 先检查录音条件和任务是否适合分析，再根据自己的具体目标、使用体验和必要时的专业反馈选择内容。低分不自动意味着训练不足；高分也不提供健康保证。

## 阅读路径

| 模块 | 篇数 | 主要内容 |
|---|---:|---|
| Module 01：算法规则 | 15 | 解释当前加权、封顶、加分与缺失值行为，区分产品规则和生理结论 |
| Module 02：分数与练习安排 | 8 | 理解分数区间，安排短时探索和日常迁移；分数不划分临床学习阶段 |
| Module 03：声音维度 | 10 | 音高、音色、自然听感、共振峰、响度与有效语音；先确认推荐是否适用 |
| Module 04：男性向声音 | 5 | 个人目标、日常表达、未使用及使用睾酮时的声音探索 |
| Module 05：非二元与多元探索 | 2 | 自定目标和场景切换；身份与“暂不确定”设置分别理解 |
| Module 06：A/B 复测 | 3 | 分数下降、听感与分数不一致、无法判断时的具体处理 |
| Module 07：录音质量 | 2 | 削波、数字电平、背景干扰与设备条件 |
| Module 08：健康与专业支持 | 4 | 发声卫生、症状分级、专业评估与 TWVQ 自评用途 |

初次使用可先读 `RULE-CONTINUOUS-01`；分数与体验冲突可读 `PRACTICE-AB-SUBJECTIVE-01`；希望了解持续元音和 F1–F4 可读 `METRIC-VFP-DARK-01`。这些是稳定的检索 ID，部分文件名保留了修订前的标题，实际展示以文章首行标题为准。

## 来源与证据范围

- [ASHA：Gender Affirming Voice and Communication](https://www.asha.org/practice-portal/professional-issues/gender-affirming-voice-and-communication/)：专业实践资料，讨论以个人为中心的声音与沟通支持，不验证 Pitchee 的分数和阈值。
- [A Study on Reliability and Validity of the Simplified Chinese Version of the Trans Woman Voice Questionnaire](https://pubs.asha.org/doi/10.1044/2022_JSLHR-21-00685)：TWVQ 简体中文版信效度研究。不是性别识别率研究，也不支持本库旧版的自编分数分级。
- [Vocal Congruence Project](https://vocalcongruence.org/)：声音与个人表达一致性的资源。
- [University of Sheffield：Voice information & resources](https://sites.google.com/sheffield.ac.uk/transvoiceandcommunicationcafe/voice-information-resources)：大学项目的声音与沟通资源导航。
- [University of Cincinnati：TruVox](https://ceas5.uc.edu/transvoice)：声音反馈工具及教学资源，使用条件和适用语言需要单独核对。
- [RLE Wiki：嗓音女性化练习](https://rle.wiki/others/voice-feminisation-exercise/)、[嗓音学习指南](https://voice.cntt.uk/)、[TransNavi：Practice for changing your voice](https://transnavi.jp/en/voice/)：社区或实践学习资料。动作比喻、个人经验和效果主张需与研究证据区分。
- [跨与多元性别档案](https://digital.transchinese.org/)：历史与社区资料入口，收录不代表内容已经过科学审查。
- [Gender Perception After Raising Vowel Fundamental and Formant Frequencies: Considerations for Oral Resonance Research](https://pubmed.ncbi.nlm.nih.gov/28844651/)：操控特定元音声学参数的感知研究；没有提供经验证的通用 F1–F4 评分公式。
- [Praat：Sound: To Formant (burg)...](https://www.fon.hum.uva.nl/praat/manual/Sound__To_Formant__burg____.html)：共振峰估计方法及参数说明，用于理解测量限制。

每篇末尾列出实际使用的资料及支持范围。产品公式以源码为依据；它们不是临床处方。论文摘要、完整论文、资料导航和社区教学应按各自性质引用，不以一个首页链接替代不存在的论文题名。

## 编辑与构建

文章使用以下四个固定二级标题：

1. `一、理解这项主题`
2. `二、练习前的观察`
3. `三、可尝试的方法`
4. `四、依据与延伸阅读`

头部包含适用场景、适用人群、核心目标及修订日期。标题和正文采用平实语言，避免贬损声线、固定性别气质、保证见效的数字及由模型分数推断器官状态。练习应说明可选择性和观察目标；不能仅用一段通用免责声明替代准确正文。

在此文章仓库目录运行：

```bash
python3 build-voice-training-library.py
```

生成本目录的 `voice-training-library.json` 和 `voice-rule-matching-matrix.json`。在 iOS 仓库运行 `python3 Scripts/build-voice-training-library.py`，默认从 `Docs/Voice-Training-Library` 生成 App 资源并同步该来源目录；可用 `ARTICLES_DIR` 显式指定其他来源。构建不会自动覆盖旁边另一份 Articles 检出。`bash Scripts/test-voice-training-library.sh` 验证文章结构、资源与推荐匹配。

49 个文章 ID、17 个检索分类和 JSON 结构保持兼容。匹配索引决定入口，不证明某篇练习适合某个人；App 推荐和全文都应允许用户依据听感及目标放弃不适用的建议。
