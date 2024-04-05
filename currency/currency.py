import cv2
import numpy as np
import onnxruntime as ort

def preprocess(frame):
    """
    Preprocess the frame for the ONNX model.
    - Resize the frame to 640x640 pixels as expected by the model.
    - Normalize if necessary.
    """
    # Resize the frame to 640x640
    resized_frame = cv2.resize(frame, (640, 640))

    # Assuming your model needs the image in CHW format
    # Normalize and transpose the frame if necessary
    # Example normalization (if your model expects values in [0,1] or mean/std normalized)
    normalized_frame = resized_frame / 255.0

    # Transpose frame from HWC to CHW format if required by your model
    transposed_frame = normalized_frame.transpose(2, 0, 1)
    
    # Add batch dimension (ONNX models typically expect a batch dimension)
    input_tensor = np.expand_dims(transposed_frame, axis=0).astype('float32')
    
    return input_tensor

def postprocess(outputs):
    # Assuming outputs[0] is the relevant output tensor
    output_tensor = outputs[0]

    # If your model outputs a multi-dimensional tensor, you might need to adjust how you access its contents.
    # For example, if it's a 1D array wrapped in an extra dimension:
    if output_tensor.ndim > 1 and output_tensor.shape[0] == 1:
        # Simplify the tensor to 1D if the first dimension is size 1
        confidence_scores = output_tensor.flatten()
    else:
        confidence_scores = output_tensor

    # Continue with confidence score processing
    max_confidence_index = np.argmax(confidence_scores)
    max_confidence_score = confidence_scores[max_confidence_index]

    if max_confidence_score > 0.5:  # Adjust threshold as necessary
        return f"Egyptian Currency Detected with confidence {max_confidence_score}"
    else:
        return "No Currency Detected"

# Load ONNX model
onnx_model_path =r"E:\DR BAHAA\The Glasses\currency\resnet50v2_weights_tf_dim_ordering_tf_kernels_notop.h5"  # Update this path
session = ort.InferenceSession(onnx_model_path)

# Start capturing video from the default camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Break the loop if there are no more frames

    # Preprocess the frame
    input_tensor = preprocess(frame)

    # Prepare the input according to your model's input name
    inputs = {session.get_inputs()[0].name: input_tensor}

    # Run inference
    outputs = session.run(None, inputs)

    # The rest of your loop here, including post-processing and displaying the frame

    
    # Postprocess and display result
    result_text = postprocess(outputs)
    cv2.putText(frame, result_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow('Frame', frame)
    
    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
