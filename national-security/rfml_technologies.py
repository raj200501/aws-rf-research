import numpy as np

def simulate_rf_signals():
    frequencies = np.linspace(1e6, 1e9, 100)
    signal_strengths = np.random.rand(100)
    return frequencies, signal_strengths

def analyze_rf_signals(frequencies, signal_strengths):
    return np.mean(signal_strengths), np.std(signal_strengths)

if __name__ == "__main__":
    frequencies, signal_strengths = simulate_rf_signals()
    mean_strength, std_strength = analyze_rf_signals(frequencies, signal_strengths)
    print(f"Mean Signal Strength: {mean_strength}")
    print(f"Standard Deviation of Signal Strength: {std_strength}")
