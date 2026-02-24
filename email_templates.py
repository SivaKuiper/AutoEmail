from datetime import datetime

def daily_report_html(inventory_data, sales_data):
    """Generate daily report email HTML"""
    
    # Group inventory by quality and status
    raw_slabs = [s for s in inventory_data if s.get('status') == 'RAW']
    polished_slabs = [s for s in inventory_data if s.get('status') == 'POLISHED']
    
    # Calculate totals
    total_raw_sqft = sum(float(s.get('raw_sqft', 0) or 0) for s in raw_slabs)
    total_polished_sqft = sum(float(s.get('polished_sqft', 0) or 0) for s in polished_slabs)
    
    # Sales summary
    total_sales_value = sum(float(s.get('total_value', 0) or 0) for s in sales_data)
    total_sales_sqft = sum(float(s.get('final_sqft', 0) or 0) for s in sales_data)
    
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; margin: 0; padding: 0; }}
            .header {{ background: linear-gradient(135deg, #00e676, #00e5ff); padding: 30px 20px; text-align: center; }}
            .header h1 {{ margin: 0; color: #000; font-size: 28px; }}
            .header p {{ margin: 5px 0 0 0; color: #000; font-size: 14px; }}
            .container {{ max-width: 600px; margin: 0 auto; }}
            .section {{ margin: 20px; padding: 20px; background: #f9f9f9; border-left: 4px solid #00e676; border-radius: 8px; }}
            .section h2 {{ margin-top: 0; color: #00e676; font-size: 20px; }}
            .metrics {{ display: flex; flex-wrap: wrap; gap: 15px; margin: 15px 0; }}
            .metric {{ flex: 1; min-width: 120px; text-align: center; background: white; padding: 15px; border-radius: 8px; }}
            .metric-value {{ font-size: 28px; font-weight: bold; color: #00e676; }}
            .metric-label {{ font-size: 11px; color: #666; text-transform: uppercase; margin-top: 5px; }}
            .footer {{ text-align: center; padding: 20px; color: #666; font-size: 12px; background: #f5f5f5; }}
            .footer a {{ color: #00e676; text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📊 FACTORY Daily Inventory Report</h1>
                <p>{datetime.now().strftime('%A, %B %d, %Y')}</p>
            </div>
            
            <div class="section">
                <h2>💎 Available Inventory</h2>
                <div class="metrics">
                    <div class="metric">
                        <div class="metric-value">{len(polished_slabs)}</div>
                        <div class="metric-label">Polished Slabs</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">{total_polished_sqft:.0f}</div>
                        <div class="metric-label">SQFT Ready</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">{len(raw_slabs)}</div>
                        <div class="metric-label">Raw Slabs</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">{total_raw_sqft:.0f}</div>
                        <div class="metric-label">SQFT Unpolished</div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>💰 Today's Sales</h2>
                <div class="metrics">
                    <div class="metric">
                        <div class="metric-value">{len(sales_data)}</div>
                        <div class="metric-label">Slabs Sold</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">{total_sales_sqft:.0f}</div>
                        <div class="metric-label">SQFT Sold</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">₹{total_sales_value/100000:.2f}L</div>
                        <div class="metric-label">Revenue</div>
                    </div>
                </div>
            </div>
            
            <div class="footer">
                <p>This is an automated report from Kriya Granite Inventory System</p>
                <p><a href="https://your-app.netlify.app">View Live Inventory →</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html

def block_completion_html(block_id, slabs_data):
    """Generate block completion email HTML"""
    
    total_slabs = len(slabs_data)
    polished_slabs = [s for s in slabs_data if s.get('status') == 'POLISHED']
    total_sqft = sum(float(s.get('polished_sqft', 0) or 0) for s in polished_slabs)
    
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; color: #333; margin: 0; padding: 0; }}
            .header {{ background: #00e676; padding: 30px 20px; text-align: center; }}
            .header h1 {{ margin: 0; color: #000; font-size: 28px; }}
            .container {{ max-width: 600px; margin: 0 auto; }}
            .section {{ margin: 20px; padding: 20px; background: #f9f9f9; border-radius: 8px; }}
            .section h2 {{ color: #00e676; }}
            .metrics {{ display: flex; gap: 20px; margin: 20px 0; }}
            .metric {{ flex: 1; text-align: center; background: white; padding: 20px; border-radius: 8px; }}
            .metric-value {{ font-size: 32px; font-weight: bold; color: #00e676; }}
            .metric-label {{ font-size: 12px; color: #666; margin-top: 5px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>✅ Block Completed - {block_id}</h1>
            </div>
            
            <div class="section">
                <h2>📊 Summary</h2>
                <div class="metrics">
                    <div class="metric">
                        <div class="metric-value">{total_slabs}</div>
                        <div class="metric-label">Total Slabs</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">{len(polished_slabs)}</div>
                        <div class="metric-label">Polished</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">{total_sqft:.0f}</div>
                        <div class="metric-label">Total SQFT</div>
                    </div>
                </div>
                
                <p><strong>Status:</strong> Available for sale immediately</p>
                <p><strong>Completion Date:</strong> {datetime.now().strftime('%B %d, %Y')}</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    return html
