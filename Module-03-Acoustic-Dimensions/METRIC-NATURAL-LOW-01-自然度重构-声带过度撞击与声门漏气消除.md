# 【自然度重构】为什么自然度偏低？解析声带过度撞击与声门漏气消除

- **适用场景**：用户在测试中自然度（Naturalness）指标长期低于 70 分，虽然音高和共鸣在及格线附近，但声音听起来沙哑、毛糙、机械或带有严重的破风气声。
- **声学机制**：声带接触不对称、声门闭合不全（Glottal Chink）或过度内收硬碰撞带来的高频谐噪比（HNR）恶化。
- **核心目标**：平复声门微湍流噪波，重塑规整对称的黏膜振动周期。

---

## 一、声学机制与算法原理

Pitchee 的自然度模型并非单纯看“音调高不高”，而是深度卷积神经网络对说话人声带振动纯净度的敏锐体察：
1. **声门噪波过高（Low Harmonic-to-Noise Ratio）**：
   - 如果声带闭合漏气，未调制的气流会形成连续的宽带白噪声（类似老旧收音机沙沙底噪），模型会立刻判定声音“不纯净”；
2. **微周期剧烈跳动（High Perturbation / Jitter & Shimmer）**：
   - 如果声带由于发紧而在每毫秒之间的振动周期时宽忽长忽短，波形形态缺乏连续性，自然度得分会骤降；
3. **声带硬起音碰撞（Vocal Fry / Glottal Shock）**：
   - 机械性的硬碰或过度的气泡音碎裂，会产生大量非周期性的脉冲尖峰。

---

## 二、症状自查与代偿排查

### 纠偏方向 A：针对“过度漏气沙哑型（Breathy）”
- **表现**：声音虽然温柔，但虚弱无力，像在严重感冒中说话，自然度常在 50–65 分。

---

## 三、训练动作与实操指南
- **探索动作**：
  1. **声门内收激活**：通过轻促的停顿音练习：“1、2、3、4”（每个数字干净利落结尾，不要带尾随拖音气流）；
  2. **SOVTE 阻抗训练**：每天进行 3 分钟吸管水泡发声，物理倒逼声带两侧后部的软骨间部闭合。

### 纠偏方向 B：针对“过度挤捏硬卡型（Pressed / Strained）”
- **表现**：声音紧绷发直、像被掐住嗓子，自然度常在 40–50 分（濒临封顶）。
- **探索动作**：
  1. **哈气叹息过渡**：在每个句子的开头，先轻微吐出一口微弱的暖风，再让声音搭在暖风上滑出；
  2. **下颌咀嚼发声法（Chewing Method）**：一边模仿大口咀嚼食物（下巴做生动的上下画圈运动），一边随意哼鸣说话，强制打碎颈部咬肌的静态痉挛。

---


---

## 四、权威文献与延伸参考
- **ASHA Practice Portal**: 《Acoustic Voice Assessment: Jitter, Shimmer and HNR》([链接](https://www.asha.org/practice-portal/professional-issues/gender-affirming-voice-and-communication/))
- **University of Sheffield**: 《Naturalness, Ease and Vocal Clarity Guide》([链接](https://sites.google.com/sheffield.ac.uk/transvoiceandcommunicationcafe/voice-information-resources))
