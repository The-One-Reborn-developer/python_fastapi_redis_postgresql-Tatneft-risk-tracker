async def close_connection(conn) -> bool:
    """
    Closes the connection to the database.

    Args:
        conn: The connection to be closed.

    Returns:
        bool: True if the connection was closed successfully, False if an error occurred.
    """
    try:
        await conn.close()
        return True
    except Exception as e:
        print(f"Error closing connection: {e}")
        return False