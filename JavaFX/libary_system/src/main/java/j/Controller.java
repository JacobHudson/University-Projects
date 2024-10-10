package j;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import java.sql.*;

public class Controller {
    public TableView<Book> tableView;
    public TableColumn<Book, Integer> idColumn;
    public TableColumn<Book, String> titleColumn;
    public TableColumn<Book, String> authorColumn;
    public TableColumn<Book, String> isbnColumn;
    public TableColumn<Book, String> availableColumn;

    public TextField titleField;
    public TextField authorField;
    public TextField isbnField;
    public Button addButton;
    public Button checkOutButton;
    public Button checkInButton;

    private ObservableList<Book> bookList;

    public void initialize() {
        // Initialize table columns
        idColumn.setCellValueFactory(new PropertyValueFactory<>("id"));
        titleColumn.setCellValueFactory(new PropertyValueFactory<>("title"));
        authorColumn.setCellValueFactory(new PropertyValueFactory<>("author"));
        isbnColumn.setCellValueFactory(new PropertyValueFactory<>("isbn"));
        availableColumn.setCellValueFactory(new PropertyValueFactory<>("available"));

        // Load books from database
        loadBooks();
    }

    private void loadBooks() {
        try {
            bookList = FXCollections.observableArrayList(BookDAO.getAllBooks());
            tableView.setItems(bookList);
        } catch (Exception e) {
            showAlert(Alert.AlertType.ERROR, "Error", "Could not load books.");
            e.printStackTrace();
        }
    }

    public void addBook(ActionEvent event) {
        String title = titleField.getText().trim();
        String author = authorField.getText().trim();
        String isbn = isbnField.getText().trim();

        if (title.isEmpty() || author.isEmpty() || isbn.isEmpty()) {
            showAlert(Alert.AlertType.WARNING, "Input Error", "Please fill all fields.");
            return;
        }

        try {
            BookDAO.addBook(title, author, isbn);
            loadBooks();
            titleField.clear();
            authorField.clear();
            isbnField.clear();
            showAlert(Alert.AlertType.INFORMATION, "Success", "Book added successfully.");
        } catch (SQLException e) {
            if (e.getMessage().contains("UNIQUE constraint failed")) {
                showAlert(Alert.AlertType.ERROR, "Error", "ISBN must be unique.");
            } else {
                showAlert(Alert.AlertType.ERROR, "Error", "Could not add book.");
                e.printStackTrace();
            }
        } catch (Exception e) {
            showAlert(Alert.AlertType.ERROR, "Error", "Could not add book.");
            e.printStackTrace();
        }
    }

    public void checkOutBook(ActionEvent event) {
        Book selectedBook = tableView.getSelectionModel().getSelectedItem();
        if (selectedBook == null) {
            showAlert(Alert.AlertType.WARNING, "No Selection", "Please select a book to check out.");
            return;
        }

        if (selectedBook.getAvailable().equals("No")) {
            showAlert(Alert.AlertType.WARNING, "Unavailable", "Book is already checked out.");
            return;
        }

        try {
            BookDAO.updateBookAvailability(selectedBook.getId(), false);
            BookDAO.addTransaction(selectedBook.getId(), "checkout");
            loadBooks();
            showAlert(Alert.AlertType.INFORMATION, "Success", "Book checked out successfully.");
        } catch (Exception e) {
            showAlert(Alert.AlertType.ERROR, "Error", "Could not check out book.");
            e.printStackTrace();
        }
    }

    public void checkInBook(ActionEvent event) {
        Book selectedBook = tableView.getSelectionModel().getSelectedItem();
        if (selectedBook == null) {
            showAlert(Alert.AlertType.WARNING, "No Selection", "Please select a book to check in.");
            return;
        }

        if (selectedBook.getAvailable().equals("Yes")) {
            showAlert(Alert.AlertType.WARNING, "Already Available", "Book is already available.");
            return;
        }

        try {
            BookDAO.updateBookAvailability(selectedBook.getId(), true);
            BookDAO.addTransaction(selectedBook.getId(), "checkin");
            loadBooks();
            showAlert(Alert.AlertType.INFORMATION, "Success", "Book checked in successfully.");
        } catch (Exception e) {
            showAlert(Alert.AlertType.ERROR, "Error", "Could not check in book.");
            e.printStackTrace();
        }
    }

    private void showAlert(Alert.AlertType type, String title, String message) {
        Alert alert = new Alert(type);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }
}
