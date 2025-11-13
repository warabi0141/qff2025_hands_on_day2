import matplotlib.pyplot as plt
import numpy as np

def plot_qubit1(rQuantum0=1.0, rQuantum1=0, angle0=0, angle1=0):
    gap=2
    R=0.7
    figsize=(4,2)
    """
    量子ビットの図を描画する関数（rQuantum0, rQuantum1は規格化値 0-1）
    
    Parameters:
    -----------
    rQuantum0 : float
        |0⟩ 内側の円の規格化半径（0-1）
    rQuantum1 : float
        |1⟩ 内側の円の規格化半径（0-1）
    angle0 : float
        |0⟩ の棒の角度（度）
    angle1 : float
        |1⟩ の棒の角度（度）
    gap : float
        左右の円の中心間距離
    R0 : float
        |0⟩ の円の固定半径
    R1 : float
        |1⟩ の円の固定半径
    figsize : tuple
        図のサイズ
    """
    
    # 内側の円の実際の半径
    r0 = R * rQuantum0
    r1 = R * rQuantum1
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # |0⟩
    circle0 = plt.Circle((0,0), R, edgecolor='black', facecolor='none', lw=2)
    ax.add_patch(circle0)
    if r0 > 0:
        inner0 = plt.Circle((0,0), r0, color='cornflowerblue')
        ax.add_patch(inner0)
        # 棒の端点を角度に沿って計算
        angle0_rad = np.radians(angle0)
        x_end0 = 0 + R * np.sin(angle0_rad)
        y_end0 = 0 + R * np.cos(angle0_rad)
        ax.plot([0, x_end0], [0, y_end0], color='black', lw=2)
    ax.text(0, -R-0.15, "|0⟩", color='black', fontsize=12, ha='center', va='top')
    
    # |1⟩
    circle1 = plt.Circle((gap,0), R, edgecolor='black', facecolor='none', lw=2)
    ax.add_patch(circle1)
    if r1 > 0:
        inner1 = plt.Circle((gap,0), r1, color='mediumturquoise')
        ax.add_patch(inner1)
        # 棒の端点を角度に沿って計算
        angle1_rad = np.radians(angle1)
        x_end1 = gap + R * np.sin(angle1_rad)
        y_end1 = 0 + R * np.cos(angle1_rad)
        ax.plot([gap, x_end1], [0, y_end1], color='black', lw=2)
    ax.text(gap, -R-0.15, "|1⟩", color='black', fontsize=12, ha='center', va='top')
    
    # 軸範囲
    ax.set_xlim(-1, gap+1)
    ax.set_ylim(-1, R+0.5)
    
    plt.show()


def plot_qubit2(
    rQuantum00=1, rQuantum01=0, rQuantum10=0, rQuantum11=0,
    angle00=0, angle01=0, angle10=0, angle11=0
):
    R=0.7
    gap=2
    figsize=(4,6)
    """
    2量子ビットの状態を2x2グリッドで描画
    
    Parameters
    ----------
    rQuantumXY : float
        内側の円の規格化半径 (0-1)
    angleXY : float
        棒の角度 (度)
    R : float
        外側の円の半径
    gap : float
        円の中心間距離
    figsize : tuple
        図のサイズ
    """
    
    states = [
        {"r": rQuantum00, "angle": angle00, "label":"00", "pos": (0, gap)},
        {"r": rQuantum01, "angle": angle01, "label":"01", "pos": (gap, gap)},
        {"r": rQuantum10, "angle": angle10, "label":"10", "pos": (0, 0)},
        {"r": rQuantum11, "angle": angle11, "label":"11", "pos": (gap, 0)},
    ]
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('#111')
    
    colors = ["cornflowerblue", "mediumturquoise", "lightgreen", "salmon"]
    
    for i, state in enumerate(states):
        x0, y0 = state["pos"]
        r = R * state["r"]
        # 外円
        circle = plt.Circle((x0, y0), R, edgecolor='black', facecolor='none', lw=2)
        ax.add_patch(circle)
        # 内円
        if r > 0:
            inner = plt.Circle((x0, y0), r, color=colors[i])
            ax.add_patch(inner)
            # 棒
            angle_rad = np.radians(state["angle"])
            x_end = x0 + R * np.sin(angle_rad)
            y_end = y0 + R * np.cos(angle_rad)
            ax.plot([x0, x_end], [y0, y_end], color='black', lw=2)
        # ラベル
        ax.text(x0, y0-R-0.15, f"|{state['label']}⟩", color='black', fontsize=12, ha='center', va='top')
    
    ax.set_xlim(-1, gap+R+1)
    ax.set_ylim(-1, gap+R+1)
    plt.show()