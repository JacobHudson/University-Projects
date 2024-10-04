package j;
public class CounterController {
    private Counter model;

    public CounterController(Counter model) {
        this.model = model;
    }

    public void handleIncrement() {
        model.increment();
    }

    public int getCount() {
        return model.getCount();
    }
}
