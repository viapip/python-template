from pathlib import Path
import yaml
from typing import Any, Dict

class Config:
    """Configuration management class"""
    
    def __init__(self, config_path: str | Path):
        self.config_path = Path(config_path)
        self.config_data: Dict[str, Any] = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")
        
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get value from configuration"""
        return self.config_data.get(key, default)
    
    @property
    def data(self) -> Dict[str, Any]:
        """Get all configuration data"""
        return self.config_data