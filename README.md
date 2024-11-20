<h1>Dynamic Excel Visualizer</h1>
    <p>
        This application is a Streamlit-based web app for dynamically visualizing data from uploaded Excel or CSV files. 
        It detects column types, suggests suitable visualizations, and allows users to create custom visualizations.
    </p>

<h2>Features</h2>
    <ul>
        <li>Upload CSV or Excel files.</li>
        <li>Preview the uploaded dataset.</li>
        <li>Automatic detection of column types (numeric, categorical, datetime, or text).</li>
        <li>Custom visualization options, including bar, scatter, line, box, violin, histogram, and count plots.</li>
        <li>Suggestions for visualizations based on the dataset.</li>
    </ul>

<h2>How to Use</h2>
    <ol>
        <li>Run the script using the command: <code>streamlit run your_script_name.py</code>.</li>
        <li>Upload a CSV or Excel file using the upload button in the sidebar.</li>
        <li>View the dataset preview in the main interface.</li>
        <li>Select the type of visualization you want to create and configure the axes.</li>
        <li>Click "Generate Visualization" to display your custom chart.</li>
        <li>View and explore suggested visualizations by enabling their respective checkboxes.</li>
    </ol>

<h2>Visualization Types</h2>
    <ul>
        <li><strong>Bar Plot:</strong> Compare values grouped by categories.</li>
        <li><strong>Scatter Plot:</strong> Show relationships between two numeric variables.</li>
        <li><strong>Line Plot:</strong> Visualize trends over time or ordered data.</li>
        <li><strong>Box Plot:</strong> Display distribution and outliers of data.</li>
        <li><strong>Violin Plot:</strong> Combine box plot and kernel density estimation.</li>
        <li><strong>Histogram:</strong> Display the frequency distribution of a numeric variable.</li>
        <li><strong>Count Plot:</strong> Count occurrences of categorical values.</li>
    </ul>

<h2>Requirements</h2>
    <p>To run this application, install the following Python packages:</p>
    <ul>
        <li>Streamlit</li>
        <li>Pandas</li>
        <li>Matplotlib</li>
        <li>Seaborn</li>
        <li>NumPy</li>
    </ul>
    <p>You can install them using pip:</p>
    <pre><code>pip install streamlit pandas matplotlib seaborn numpy</code></pre>

<h2>Code Highlights</h2>
    <p>The app is designed with the following key functionalities:</p>
    <ul>
        <li><code>detect_column_types</code>: Automatically identifies the type of data in each column.</li>
        <li><code>validate_columns</code>: Ensures selected columns exist in the dataset.</li>
        <li><code>create_visualization</code>: Generates the requested visualization using Seaborn and Matplotlib.</li>
        <li><code>suggest_visualizations</code>: Provides recommendations for visualizations based on column types.</li>
    </ul>

<h2>License</h2>
    <p>This project is open source and available for modification and distribution under an MIT License.</p>

<h2>Contact</h2>
    <p>For questions or suggestions, please reach out via GitHub or email.</p>
