# 8 — 分步证明文字

## 步骤 0：Step 0：题设条件与几何构型

设锐角 △ABC 的外心为 O，垂心为 H。△ABC 内部任取一点 P，其关于三边 BC, CA, AB 的轴对称点分别为 D, E, F。求证目标：S△HDE / S△HDF = S△OAB / S△OAC。

## 步骤 1：Step 1：构造圆 ⊙(AHC) 与割线交点 E'

垂心 H 关于边 AC 的对称点在外接圆 ⊙O 上，故圆 ⊙(AHC) 恰为 ⊙O 关于直线 AC 的对称圆，其半径亦为 R。延长射线 AE 与圆 ⊙(AHC) 交于点 E'。

## 步骤 2：Step 2：圆周角平移导出 EF ∥ E'H

由轴对称得 AP = AF = AE，顶角 ∠EAF = 2∠BAC = 2A，故等腰底角 ∠AEF = 90° - A。由高线知 ∠ACH = 90° - A；又在圆 ⊙(AHC) 中，同弧圆周角 ∠AE'H = ∠ACH = 90° - A。同位角相等得出：EF ∥ E'H！

## 步骤 3：Step 3：同底等高平行割补面积转换

因为 EF ∥ E'H，点 H 与点 E' 到直线 EF 的垂直高度严格相等。利用公共底边 EF 上的平行滑移变形，立即得到面积等式：S△HEF = S△EE'F。将垂心三角形成功转化到射线割线上的三角形！

## 步骤 4：Step 4：圆幂不变性求解 S△HEF

由正弦定理：S△EE'F = ½ EF · EE' · sin ∠FEA = ½ AE · EE' · sin 2A。核心几何洞察：E 与圆 ⊙(AHC) 是点 P 与外接圆 ⊙O 关于边 AC 的轴对称图形！因此割线幂之积 AE · EE' 严格等于点 P 对圆 ⊙O 的圆幂绝对值 IP = |R² - OP²|！故 S△HEF = ½ · IP · sin 2A。

## 步骤 5：Step 5：三边对称轮换导出面积闭式

完全同理，关于边 BC（对应顶角 C）与边 AB（对应顶角 B）分别进行平行割补与圆幂映射，立即得到：S△HDE = ½ · IP · sin 2C，S△HDF = ½ · IP · sin 2B。两式作比消去圆幂因子：S△HDE / S△HDF = sin 2C / sin 2B。

## 步骤 6：Step 6：外心三角形面积与最终命题得证

在外接圆 ⊙O 中，半径 OA = OB = OC = R。圆心角 ∠AOB = 2C, ∠AOC = 2B。故外心三角形面积为：S△OAB = ½ R² sin 2C，S△OAC = ½ R² sin 2B。两式作比消去 ½ R² 同样得到 sin 2C / sin 2B！综合结论：S△HDE / S△HDF = S△OAB / S△OAC，原命题完美得证！
