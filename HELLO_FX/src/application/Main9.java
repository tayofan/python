package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.stage.Stage;


public class Main9 extends Application {
	Button btn;
	TextField tf_my;
	TextField tf_com;
	TextField tf_result;
	
	@Override
	public void start(Stage primaryStage) {
		try {
			Parent root = FXMLLoader.load(getClass().getResource("main9.fxml"));
			Scene scene = new Scene(root,400,400);
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			tf_my = (TextField)scene.lookup("#tf_my");
			tf_com = (TextField)scene.lookup("#tf_com");
			tf_result = (TextField)scene.lookup("#tf_result");
			btn = (Button)scene.lookup("#btn");
			
			tf_my.setOnKeyPressed(new EventHandler<KeyEvent>() {

				@Override
				public void handle(KeyEvent event) {
//					if(event.getCode().equals(KeyCode.ENTER)) {
					if(event.getCode().toString().equals("ENTER")) {
					
						playGame();
					}
					
				}
			
			});
			
			btn.setOnMouseClicked(new EventHandler<Event>() {

				@Override
				public void handle(Event event) {
					playGame();
					
				}
				
			});
			
			
			
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void playGame() {
		String result = "";
		String my = tf_my.getText();
		String com = "";
		
		double random = Math.random();
		if(random < 0.3) tf_com.setText("가위");
		else if(random < 0.6) tf_com.setText("바위");
		else tf_com.setText("보");
		
		String tfcom = tf_com.getText();
		
		if(my.equals("가위") && tfcom.equals("바위")) result += "졌습니다.";
		if(my.equals("가위") && tfcom.equals("가위")) result += "비겼습니다.";
		if(my.equals("가위") && tfcom.equals("보")) result += "이겼습니다.";
		
		if(my.equals("바위") && tfcom.equals("바위")) result += "비겼습니다.";
		if(my.equals("바위") && tfcom.equals("가위")) result += "이겼습니다.";
		if(my.equals("바위") && tfcom.equals("보")) result += "졌습니다.";
		
		if(my.equals("보") && tfcom.equals("바위")) result += "이겼습니다.";
		if(my.equals("보") && tfcom.equals("가위")) result += "졌습니다.";
		if(my.equals("보") && tfcom.equals("보")) result += "비겼습니다.";
		
		
		tf_result.setText(result);
	}
	
	public static void main(String[] args) {
		launch(args);
	}
}
