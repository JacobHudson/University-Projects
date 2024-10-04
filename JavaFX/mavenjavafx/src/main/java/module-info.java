module j {
    requires javafx.controls;
    requires javafx.fxml;

    opens j to javafx.fxml;
    exports j;
}
