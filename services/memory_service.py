from collections import defaultdict

sessions = defaultdict(list)


def get_session_history(session_id: str):
    return sessions[session_id]
