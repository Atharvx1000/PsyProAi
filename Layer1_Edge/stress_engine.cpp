#include <iostream>
#include <vector>
#include <chrono>
#include <numeric>
#include <cmath>

class BioKineticSentinel {
public:
    // Calculates the 'Jitter' (Variance) in millisecond timings
    double calculate_intent_variance(const std::vector<double>& intervals) {
        if (intervals.empty()) return 0.0;
        
        double sum = std::accumulate(intervals.begin(), intervals.end(), 0.0);
        double mean = sum / intervals.size();
        
        double sq_sum = 0;
        for(double val : intervals) {
            sq_sum += (val - mean) * (val - mean);
        }
        return std::sqrt(sq_sum / intervals.size()); // Standard Deviation
    }

    std::string evaluate_state(double jitter) {
        // Professional Threshold: Jitter > 15ms indicates 'Stress/Coercion'
        if (jitter > 15.0) return "HIGH_STRESS_COERCION";
        return "CALM_INTENT";
    }
};

int main() {
    BioKineticSentinel sentinel;
    
    // Real-world simulated typing gaps (ms) between keys
    // Professional data: Uneven gaps (200ms, 50ms, 400ms) suggest stress
    std::vector<double> keystroke_intervals = {102.5, 250.2, 80.1, 310.4, 110.6};

    double jitter = sentinel.calculate_intent_variance(keystroke_intervals);
    std::string result = sentinel.evaluate_state(jitter);

    // This output is captured by the Serial Pipeline
    std::cout << result << std::endl;

    return 0;
}