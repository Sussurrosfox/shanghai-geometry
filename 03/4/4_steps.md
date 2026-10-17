# 4 — 分步证明文字

## 步骤 0：基础构型：定点 A, B, C 与切线交点 P

在直线 AC 上依次取定点 A, B, C。
    构造过 A, C 的圆 Γ（圆心不在 AC 上）。
    过 A, C 作圆 Γ 的切线交于点 P。
    连结线段 PB 交圆 Γ 于点 Q，连结弦 QA, QC。

## 步骤 1：等腰 △PAC 结合正弦定理

由切线长定理知 PA = PC，故 △PAC 为等腰三角形。
    在 △PAB 和 △PCB 中分别利用正弦定理：
    
      \( \frac{AB}{\sin\angle APB} = \frac{PA}{\sin\angle PBA} \),  
      \( \frac{BC}{\sin\angle CPB} = \frac{PC}{\sin\angle PBC} \)
    
    因为 A, B, C 共线，∠PBA + ∠PBC = 180°（正弦相等），且 PA = PC，两式相比立即得出：
    
      \( \frac{AB}{BC} = \frac{\sin\angle APB}{\sin\angle CPB} \)  … (1)

## 步骤 2：角平分线 QS 与等腰 △ASC

作 ∠AQC 的平分线交 AC 于点 R，与圆 Γ 再次交于异于 Q 的一点 S。
    因为 QS 平分 ∠AQC，所以圆周角 ∠AQS = ∠CQS。
    由等圆周角对等弧，弧 AS =  弧 CS，从而弦长 SA = SC，△ASC 为等腰三角形。
    在 △ASR 和 △CSR 中应用正弦定理，同理可得：
    
      \( \frac{AR}{RC} = \frac{\sin\angle ASR}{\sin\angle CSR} = \frac{\sin\angle ASQ}{\sin\angle CSQ} \)  … (2)

## 步骤 3：弦切角定理与等角链构建

利用弦切角定理与同弧圆周角性质建立两组关键等角链：
    1) 直线 PA 切圆于 A，由弦切角定理知 ∠PAQ = ∠QCA；又弧 AS =  弧 CS，故圆周角 ∠ASQ = ∠QCA。因此：
    
      \( \angle PAQ = \angle ASQ = \angle QCA \)
    
    2) 同理，直线 PC 切圆于 C，弦切角 ∠PCQ = ∠QAC；又圆周角 ∠CSQ = ∠QAC。因此：
    
      \( \angle PCQ = \angle CSQ = \angle QAC \)

## 步骤 4：角元塞瓦定理与两式平方转换

在 △PAC 中，三射线 PB(PQ), QA, QC 共点于 Q。
    由角元形式的塞瓦定理（Trigonometric Ceva's Theorem）：
    
      \( \frac{\sin\angle APB}{\sin\angle CPB} \cdot \frac{\sin\angle QAC}{\sin\angle QAP} \cdot \frac{\sin\angle QCP}{\sin\angle QCA} = 1 \)
    
    移项代入 Step 3 的等角链：
    
      \( \frac{\sin\angle APB}{\sin\angle CPB} = \frac{\sin\angle PAQ}{\sin\angle QAC} \cdot \frac{\sin\angle QCA}{\sin\angle PCQ} = \frac{\sin^2\angle ASQ}{\sin^2\angle CSQ} \)  … (3)

## 步骤 5：最终结论：R 为定比内分点，与圆无关

综合式 (1)、式 (2) 与式 (3)：
    
      \( \frac{AB}{BC} = \frac{\sin^2\angle ASQ}{\sin^2\angle CSQ} = \left( \frac{AR}{RC} \right)^2 \)
    
    两边取算术平方根，立即得出：
    
      \( \frac{AR}{RC} = \sqrt{\frac{AB}{BC}} \)
    
    因为定点 A, B, C 固定在直线上，比值 AB / BC 是恒定的几何常数！
    因此内分比 AR / RC 唯一确定，点 R 的位置完全不依赖于圆 Γ 的选取，原命题得证！
