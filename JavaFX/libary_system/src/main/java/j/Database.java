package j;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class Database {
    private static final String DB_URL = "jdbc:sqlite:library.db";

    public static Connection connect() throws Exception {
        return DriverManager.getConnection(DB_URL);
    }

    public static void initialize() {
        String booksTable = "CREATE TABLE IF NOT EXISTS books (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "title TEXT NOT NULL," +
                "author TEXT NOT NULL," +
                "isbn TEXT UNIQUE NOT NULL," +
                "available INTEGER DEFAULT 1" +
                ");";

        String transactionsTable = "CREATE TABLE IF NOT EXISTS transactions (" +
                "id INTEGER PRIMARY KEY AUTOINCREMENT," +
                "book_id INTEGER," +
                "action TEXT CHECK(action IN ('checkin','checkout')) NOT NULL," +
                "timestamp DATETIME DEFAULT CURRENT_TIMESTAMP," +
                "FOREIGN KEY(book_id) REFERENCES books(id)" +
                ");";

        try (Connection conn = connect(); Statement stmt = conn.createStatement()) {
            stmt.execute(booksTable);
            stmt.execute(transactionsTable);
            System.out.println("Database initialized.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
