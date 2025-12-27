from modules.account_analysis import save_analysis_results

def run_analysis():
    """
    Run analysis and return analysis results
    """
    age_stats, device_stats, privacy_stats = save_analysis_results()

    return {
        "age": age_stats,
        "device": device_stats,
        "privacy": privacy_stats
    }
